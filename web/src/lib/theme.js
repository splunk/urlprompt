import React, { useState } from 'react'
import Text from '@splunk/react-ui/Text';
import Switch from '@splunk/react-ui/Switch';
import RadioList from '@splunk/react-ui/RadioList';
import Select from '@splunk/react-ui/Select';
import Slider from '@splunk/react-ui/Slider';
import Heading from '@splunk/react-ui/Heading';

const MyCustomWidget = (props) => {
    return (
      <input type="text"
        className="custom"
        value={props.value}
        required={props.required}
        onChange={(event) => props.onChange(event.target.value)} />
    );
  };
  

  const CustomTitleField = function (props) {
    return (
        <div></div>
    )
  }
  const CustomDescriptionField = function (props) {
    return (
        <div style={{fontSize: 14, color: "white"}}>{props.description}</div>
    )
  }

  const CustomText = function (props) {
    return (
        <Text canClear value={props.value} onChange={(e, {value}) => props.onChange(value)} />
    )
}

const CustomCheckbox = function (props) {
    return (
        <Switch
            key={props.value}
            value={props.value}
            onClick={() => props.onChange(!props.value)}
            selected={props.value}
            appearance="checkbox"
        >{props.label}
        </Switch>
    );
};

const CustomRadio = function (props) {
    return (
        <RadioList direction="row">
            {props.options.enumOptions.map(option => 
                <RadioList.Option key={option.value} value={option.value}>{option.label}</RadioList.Option>
            )}
        </RadioList>
        );
};

const CustomSelect = function (props) {
    console.log(props)
    return (
        <Select direction="row" value={props.value} onChange={(e, {value}) => props.onChange(value)}>
            {props.options.enumOptions.map(option => 
                <Select.Option key={option.value} value={option.value} label={option.label}></Select.Option>
            )}
        </Select>
        );
};


  const myWidgets = {
    myCustomWidget: MyCustomWidget,
    TextWidget: CustomText,
    CheckboxWidget: CustomCheckbox,
    RadioWidget: CustomRadio,
    SelectWidget: CustomSelect
  };

  const myFields = {
      TitleField: CustomTitleField,
      DescriptionField: CustomDescriptionField
  }
  
  const ThemeObject = {widgets: myWidgets, fields: myFields};
  export default ThemeObject;
  