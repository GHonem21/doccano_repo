export class ConfigItemList {
  constructor(public configItems: ConfigItem[]) {}

  static valueOf(items: ConfigItem[]): ConfigItemList {
    return new ConfigItemList(items)
  }

  toArray(): Object[] {
    return this.configItems.map(item => item.toObject())
  }
}

export class ConfigItem {
  constructor(
    public id: number,
    public modelName: string,
    public modelAttrs: object,
    public template: string,
    public labelMapping: object
  ) {}

  static valueOf(
    { id, model_name, model_attrs, template, label_mapping }:
    { id: number, model_name: string, model_attrs: object, template: string, label_mapping: object }
  ): ConfigItem {
    return new ConfigItem(id, model_name, model_attrs, template, label_mapping)
  }

  toObject(): Object {
    return {
      id: this.id,
      modelName: this.modelName,
      modelAttrs: this.modelAttrs,
      template: this.template,
      labelMapping: this.labelMapping
    }
  }
}

export const headers = [
  {
    text: 'Model name',
    align: 'left',
    value: 'modelName',
    sortable: false
  }
]
