# Prompt Schema

URLP Prompts are based on [JSON Schema](http://json-schema.org/) definitions.


## Boolean Prompt

```json
{
    "schema": {
        "title": "Convert Investigation 1223 into case",
        "description": "<supplemental information>",
        "type": "object",
        "required": ["approve"],
        "properties": {
            "approve": {"type": "boolean", "title": "Convert to case?"}
        }
    }
}
```

![Boolean Prompt](../assets/prompts/boolean_prompt.png)

## Integer Prompt

```json
{
    "schema": {
        "title": "How happy are you on a scale 1-10",
        "description": "",
        "type": "object",
        "required": ["happiness"],
        "properties": {
            "happiness": {"type": "integer", "title": "Happiness Level", "minumum": 0, "maximum": 10}
        }
    }
}
```

![Integer Prompt](../assets/prompts/integer_prompt.png)


## Combined Prompt

```json
{
    "schema": {
        "title": "Tell me something about yourself!",
        "type": "object",
        "required": ["height", "eyecolor", "birthyear"],
        "properties": {
            "height": {"type": "integer", "title": "Height in cm"},
            "birthyear": {"type": "integer", "title": "Birthyear (YYYY)"},
            "eyecolor": {
            "type:": "number",
            "enum": [1, 2, 3, 4, 5],
            "enumNames": ["blue", "grey", "green", "brown", "other"]
            }
        }
    }
}
```

![Combined Prompt](../assets/prompts/combined_prompt.png)
