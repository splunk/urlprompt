export function fetchPrompt(id) {
    return fetch(`/api/prompts/${id}/`).then(res => res.json())
}

export function answerPrompt(id, responseData) {
    console.log( { "response": responseData })
    return fetch(`/api/prompts/${id}/`, { method: 'PATCH', body: JSON.stringify({ "response": responseData }), headers: {'Content-Type': 'application/json'} }).then(res => res.json())
}