async function submitQuery() {
    const query = document.getElementById('query').value;
    const responseContainer = document.getElementById('response');

    if (!query.trim()) {
        responseContainer.innerText = "Please enter a valid query.";
        return;
    }

    try {
        const response = await fetch('/assistant/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });
        const data = await response.json();
        responseContainer.innerHTML = data.response;
    } catch (error) {
        console.error('Error:', error);
        responseContainer.innerText = "An error occurred. Please try again later.";
    }
}
