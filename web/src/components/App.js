import React from 'react'
import ColumnLayout from '@splunk/react-ui/ColumnLayout';
import { SplunkThemeProvider } from '@splunk/themes';
import Prompt from './Prompt'
import Heading from '@splunk/react-ui/Heading';

export default function App() {

    const urlParams = new URLSearchParams(window.location.search);
    const hasID = urlParams.has('id')

    return (
        <SplunkThemeProvider family="prisma" colorScheme="dark">
            <ColumnLayout>
                <ColumnLayout.Row>
                    <ColumnLayout.Column span={2}>
                    </ColumnLayout.Column>
                    <ColumnLayout.Column span={8}>
                        <Heading level={4} style={{ marginBottom: '30px', color: '#7ecd7e' }}>
                            URL Prompt for Phantom
                    </Heading>
                        {hasID && <Prompt id={urlParams.get('id')}></Prompt>}
                    </ColumnLayout.Column>
                    <ColumnLayout.Column span={2}>
                    </ColumnLayout.Column>
                </ColumnLayout.Row>
            </ColumnLayout>
        </SplunkThemeProvider>
    )
}