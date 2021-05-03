import React from 'react'
import ColumnLayout from '@splunk/react-ui/ColumnLayout';
import { SplunkThemeProvider } from '@splunk/themes';
import Prompt from './Prompt'
import Chip from '@splunk/react-ui/Chip';

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
                        <Chip appearance="secondary" style={{ marginBottom: '30px' }}>
                            URL Prompt for Phantom
                    </Chip>
                        {hasID && <Prompt id={urlParams.get('id')}></Prompt>}
                    </ColumnLayout.Column>
                    <ColumnLayout.Column span={2}>
                    </ColumnLayout.Column>
                </ColumnLayout.Row>
            </ColumnLayout>
        </SplunkThemeProvider>
    )
}