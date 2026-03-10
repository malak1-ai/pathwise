document.getElementById('skill-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const job = document.getElementById('job').value.trim();
    const industry = document.getElementById('industry').value.trim();
    const submitBtn = document.getElementById('submit-btn');
    const loader = document.getElementById('loader');
    const resultsContainer = document.getElementById('results-container');
    const skillsList = document.getElementById('skills-list');
    const solutionsList = document.getElementById('solutions-list');
    const booksList = document.getElementById('books-list');

    if (!job || !industry) return;

    // Show loading state
    submitBtn.disabled = true;
    loader.style.display = 'block';
    resultsContainer.classList.add('hidden');
    skillsList.innerHTML = '';
    solutionsList.innerHTML = '';
    booksList.innerHTML = '';

    try {
        const response = await fetch('/get-skills', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ job, industry })
        });

        const data = await response.json();

        if (response.ok) {
            let skills;
            try {
                // The AI might return a stringified JSON in the "skills" field
                skills = JSON.parse(data.skills);
            } catch (err) {
                // Fallback: If it's not valid JSON, we just treat it as text or try to clean it
                console.error("Failed to parse skills JSON:", err);
                skills = [{ skill: "Analysis Complete", explanation: data.skills }];
            }

            if (Array.isArray(skills)) {
                const allSolutions = new Set();
                const allBooks = new Set();

                skills.forEach(item => {
                    // Render Skill Card
                    const skillCard = document.createElement('div');
                    skillCard.className = 'skill-card';
                    skillCard.innerHTML = `
                        <h3 class="card-title">${item.skill}</h3>
                        <p class="card-text">${item.explanation}</p>
                    `;
                    skillsList.appendChild(skillCard);

                    // Collect Solutions and Books
                    if (item.solutions) item.solutions.forEach(s => allSolutions.add(s));
                    if (item.books) item.books.forEach(b => allBooks.add(b));
                });

                // Render Solutions
                allSolutions.forEach(sol => {
                    const solCard = document.createElement('div');
                    solCard.className = 'solution-card';
                    solCard.innerHTML = `<p class="card-text">${sol}</p>`;
                    solutionsList.appendChild(solCard);
                });

                // Render Books
                allBooks.forEach(book => {
                    const bookCard = document.createElement('div');
                    bookCard.className = 'book-card';
                    bookCard.innerHTML = `<p class="card-text"><strong>${book}</strong></p>`;
                    booksList.appendChild(bookCard);
                });
            }
            else {
                throw new Error("Invalid skills format received.");
            }

            resultsContainer.classList.remove('hidden');
            resultsContainer.scrollIntoView({ behavior: 'smooth' });
        } else {
            alert(data.error || "Something went wrong.");
        }
    } catch (error) {
        console.error("Fetch Error:", error);
        alert("Failed to connect to the server.");
    } finally {
        submitBtn.disabled = false;
        loader.style.display = 'none';
    }
});
