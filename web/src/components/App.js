import React from 'react'
import ColumnLayout from '@splunk/react-ui/ColumnLayout';
import { SplunkThemeProvider } from '@splunk/themes';
import Prompt from './Prompt'

export default function App() {
    return (
        <SplunkThemeProvider family="prisma" colorScheme="dark">
            <ColumnLayout>
                <ColumnLayout.Row>
                <ColumnLayout.Column span={2}>
                </ColumnLayout.Column>
                <ColumnLayout.Column span={8}>
                    <Prompt path="prompts/:id"></Prompt>
                    </ColumnLayout.Column>
                    <ColumnLayout.Column span={2}>
                    </ColumnLayout.Column>
                </ColumnLayout.Row>
            </ColumnLayout>
        </SplunkThemeProvider>
    )
}