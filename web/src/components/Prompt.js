import React, { useEffect, useState } from 'react'
import Button from '@splunk/react-ui/Button'
import './Prompt.css'
import { withTheme } from '@rjsf/core';
import Heading from '@splunk/react-ui/Heading'
import Message from '@splunk/react-ui/Message'
import P from '@splunk/react-ui/Paragraph';
import WaitSpinner from '@splunk/react-ui/WaitSpinner';
import DL from '@splunk/react-ui/DefinitionList';
import moment from 'moment'

import PromptTheme from '../lib/theme'
import { fetchPrompt, answerPrompt } from '../lib/api'

export default function Prompt(props) {

  const [formData, setFormData] = useState({})
  const [prompt, setPrompt] = useState({})
  const [isLoading, setIsLoading] = useState(false);

  const ThemedForm = withTheme(PromptTheme);

  useEffect(() => {
    setIsLoading(true)
    fetchPrompt(props.id).then((res) => {
      setPrompt(res)
      setIsLoading(false)
    })
  }, []);

  const onSubmit = function ({ formData }) {
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


      {prompt.schema && prompt.status !== "complete" &&
        <div>
          <Heading level={2}>{prompt.schema.title}</Heading>
          <DL style={{marginBottom: "30px"}}>
            <DL.Term>Creator</DL.Term>
            <DL.Description>{prompt.created_by.username}</DL.Description>
            <DL.Term>Time Created</DL.Term>
            <DL.Description>{moment(prompt.created_at).format('MMMM Do YYYY, h:mm:ss a')}</DL.Description>
            <DL.Term>Status</DL.Term>
            <DL.Description>{prompt.status}</DL.Description>
        </DL>
          <ThemedForm onSubmit={onSubmit} formData={formData} schema={prompt.schema}>
            <Button appearance="flat" style={{ float: "right" }} type="submit">Submit</Button>
          </ThemedForm></div>}
      {isLoading && <WaitSpinner size="large" />}

      {!isLoading && !prompt.schema && <P style={{marginLeft: '1em'}}>Prompt not found.</P>}

    </div>


  )

}