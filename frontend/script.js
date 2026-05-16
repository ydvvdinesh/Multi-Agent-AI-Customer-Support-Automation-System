async function analyzeTicket() {

    const ticket =
        document.getElementById("ticket").value;

    const response = await fetch(
        "http://127.0.0.1:8000/analyze-ticket",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                ticket: ticket
            })
        }
    );

    const data = await response.json();

    document.getElementById("output").innerHTML = `

        <div class="result">

            <div class="section">
                <div class="title">Ticket Summary</div>
                <pre>${data.summary}</pre>
            </div>

            <div class="section">
                <div class="title">Department Routing</div>
                <pre>${data.department}</pre>
            </div>

            <div class="section">
                <div class="title">Estimated Resolution Time</div>
                <pre>${data.estimated_resolution_time}</pre>
            </div>

            <div class="section">
                <div class="title">AI Resolution</div>
                <pre>${data.ai_resolution}</pre>
            </div>

            <div class="section">
                <div class="title">Similar Historical Tickets</div>

                <pre>
${data.similar_tickets.join(
"\\n\\n------------------------\\n\\n"
)}
                </pre>

            </div>

        </div>
    `;
}