import React, { useEffect, useState } from 'react'
import Button from '@splunk/react-ui/Button'
import './Prompt.css'
import { withTheme } from '@rjsf/core';
import Card from '@splunk/react-ui/Card'
import Form from "@rjsf/core";
import Message from '@splunk/react-ui/Message'

import PromptTheme from '../lib/theme'
import {fetchPrompt, answerPrompt} from '../lib/api'

export default function Prompt(props) {

    const urlParams = new URLSearchParams(window.location.search);

    const [formData, setFormData] = useState({})
    const [prompt, setPrompt] = useState({})

    const ThemedForm = withTheme(PromptTheme);
 
    useEffect(() => {
      fetchPrompt(urlParams.get('id')).then((res) => {
        setPrompt(res)
      })
    }, []);
  
    const onSubmit = function({formData}) {
        setFormData(formData)
        answerPrompt(prompt.id, formData).then(res => {
          setPrompt(res)
        })
    }

    return (
      <div>
        {prompt && prompt.status === "complete" ? <Message appearance="fill" type="success" >
                <Message.Title>
                  <strong>Prompt complete.</strong>
                </Message.Title>
                A response for this prompt has been recorded.
            </Message>
          : <div></div>
        }
           

      {prompt.schema && prompt.status !== "complete" && <Card style={{width: "100%"}}>
            <Card.Header title={prompt.schema.title} subtitle={`Created on ${prompt.created_at} by ${prompt.created_by.username}`}>
            </Card.Header>
            <Card.Body>
            <ThemedForm onSubmit={onSubmit} formData={formData} schema={prompt.schema}>
            <Button type="submit">Submit</Button>
            </ThemedForm>

            </Card.Body>
            <Card.Footer>
            </Card.Footer>
        </Card>}
        </div>
    )

}