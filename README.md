# Tech Skills & Concepts Ontology by [MIND](https://mind.index.dev/)

Welcome to the **MIND Tech Skills & Concepts Ontology** repository!  
This open-source project aims to provide a comprehensive and evolving knowledge base (ontology) of technical skills, frameworks, libraries, services, tools, and related concepts. Our goal is to help everyone—from recruiters and HR platforms to AI developers—improve how they extract, map, and match skills in the rapidly expanding tech landscape.

---

## Table of Contents
1. [Background & Motivation](#background--motivation)  
2. [What This Ontology Covers](#what-this-ontology-covers)  
3. [Structure and Highlights](#structure-and-highlights)  
4. [Sample Ontology Extract](#sample-ontology-extract)  
5. [Why Contribute?](#why-contribute)  
6. [How to Contribute](#how-to-contribute)  
7. [Usage & Integration](#usage--integration)  
8. [License](#license)  
9. [Contact & Feedback](#contact--feedback)  

---

## Background & Motivation

Skills matching at scale in recruitment is not easy. At **MIND**, we’ve iterated through multiple approaches to extract technical skills from both job descriptions and candidate CVs, aiming to match the right talent to the right opportunities. Yet, mismatches often occur. For example:
- **Synonyms**: *JSON Web Tokens* vs. *jsonwebtoken*, *React* vs. *React.js*, or minor typos like *Postgres SQL* vs. *PostgreSQL*.
- **Implied Skills**: *Next.js* implies knowledge of *React*, which implies *JavaScript*, but not every candidate or job listing explicitly states all these overlapping skills.
- **Aliases vs. Replacements**: In AI/ML, experience with any Transformer-based LLM might be more crucial than the exact brand name (e.g., *Llama*, *Mistral*, or *Gemma*).  

These pitfalls show why a single **taxonomy** of skill synonyms is insufficient. We need **hierarchies**, **categories**, and **relations** that capture how skills imply or overlap with others, and how certain conceptual aspects transfer across tasks or frameworks.

**At MIND, to build our explainable AI Recommender as a Service, we needed a rule-based knowledge set** that was granular, up-to-date, and captured all these relationships. We didn't find an open resource that was good enough, so we decided to build our own. 

After starting with a taxonomy, we have now evolved it into a full-fledged **ontology**. We are open-sourcing it because we believe this resource can help many projects, such as:
- Skills extraction and standardization
- Job / candidate matching or searching
- Generating datasets for specialized AI models
- Gaining a holistic perspective of the tech landscape
- Identifying skill gaps and mapping out career paths
- Many other use cases

---

## What This Ontology Covers

**Initial Stats**:
- **3333** _Skills_
- **974** _Concepts_
- **10897** _Relations_

**Skill Types**:
1. **Programming Languages**  
2. **Markup Languages**  
3. **Frameworks**  
4. **Libraries**  
5. **Databases & Query Languages**  
6. **Protocols**  
7. **Tools**  
8. **Services**  

**Concept Types**:
- **Architectural Patterns**  
- **Application Tasks**  
- **Application Domains**  
- **Deployment Types**  
- **Other conceptual aspects**  

**Relevant for, but not limited to**:
```
[
  "Backend",
  "Frontend",
  "Fullstack",
  "Mobile",
  "Desktop",
  "Embedded Systems",
  "Systems Programming",
  "IoT",
  "Blockchain",
  "RPA",
  "DevOps",
  "MLOps",
  "Data Engineering",
  "Data Science",
  "ML/AI",
  "Cybersecurity",
  "QA/Testing",
  "Networking",
  "Game Development"
]
```

We decided to focus on an **open, living resource** that can evolve as new technologies, frameworks, and libraries appear.

---

## Structure and Highlights

1. **Relationships & Implied Knowledge**:  
   - A skill like **Next.js** implies knowledge of **React**, which itself implies knowledge of **JavaScript**. This hierarchical structure helps avoid missed matches.

2. **Synonyms and Common Misspellings**:  
   - You’ll see synonyms like “jsonwebtoken” and “JWT” mapped to the same concept. Typos or variations like “node mailer” vs. “nodemailer” are captured to reduce search inaccuracies.

3. **Conceptual Aspects**:  
   - Some skills revolve around **conceptual** or **domain** knowledge (e.g., “LLM-based AI,” “Email and Notification Services”). These aspects are important to identify “transferable” or “broad” skill coverage.

4. **Custom Python Classes**:  
   - The code includes classes such as `Skill`, `ProgrammingLanguage`, `Framework`, `Library`, `Database`, `Tool`, `Service`, etc. Each defines properties and relationships relevant to that category (e.g. `impliesKnowingSkills`, `deploymentType`, `solvesApplicationTasks`).

5. **Taxonomy Loader & Merger**:  
   - The `Taxonomy` class provides loading, merging, and validating logic. It ensures synonyms are tracked in a case-insensitive manner and that references to known application domains, architectural patterns, or conceptual aspects are correct.

---

## Sample Ontology Extract

Below is a short excerpt showing how each skill node might look in JSON. Notice the fields like `synonyms`, `impliesKnowingSkills`, and `solvesApplicationTasks`.  

```jsonc
{
  "name": "engine.io",
  "synonyms": [
    "engine.io",
    "engine io"
  ],
  "type": ["Library"],
  "technicalDomains": ["Backend"],
  "impliesKnowingSkills": [],
  "impliesKnowingConcepts": [],
  "conceptualAspects": [],
  "architecturalPatterns": [],
  "supportedProgrammingLanguages": ["JavaScript"],
  "associatedToApplicationDomains": [],
  "solvesApplicationTasks": [
    "Streaming and Real-time Processing"
  ]
}
```

```jsonc
{
  "name": "Svelte",
  "synonyms": [
    "svelte",
    "svelte.js",
    "svelte js"
  ],
  "type": ["Framework"],
  "technicalDomains": ["Frontend"],
  "impliesKnowingSkills": [
    "HTML",
    "CSS",
    "SvelteKit",
    "Rollup",
    "JavaScript"
  ],
  "implementsPatternsByDefault": [
    "Component-Based Architecture",
    "Single Page Application (SPA)"
  ],
  "associatedToApplicationDomains": []
}
```

---

## Why Contribute?

- **Shape the Tech Landscape**: By helping standardize skill definitions, you actively improve how recruiters, HR systems, and AI tools understand and leverage tech capabilities.  
- **Reduce Ambiguities & Typos**: If you’ve ever seen mismatches due to synonyms or slight variations, here’s your chance to fix them for everyone.  
- **Add Missing Skills**: New frameworks and languages appear regularly. Keep the ontology fresh and up-to-date.  
- **Improve AI Training Data**: Many ML/AI applications can benefit from well-labeled data on skill relationships and synonyms.  

---

## How to Contribute

1. **Fork and Clone**: Fork this repository and clone it locally to work on updates.  
2. **Add or Modify Skills**:  
   - If you spot a missing skill or concept, create or update a JSON file under `./skills/` or `./concepts/`.  
   - Ensure synonyms, implied skills, and conceptual aspects are correct and add references where possible.  
3. **Code Changes**: If you’re improving the Python classes or taxonomy logic, please ensure you add any relevant tests.  
4. **Open a Pull Request**:  
   - Describe the changes you made and the reasons behind them.  
   - Tag any relevant issues if the changes fix or update them.  
5. **Feedback and Discussion**:  
   - If you’re not sure about something or have a question, open an Issue. We can work together to refine the definitions.  

We welcome bug reports, suggestions, or large-scale expansions. Nothing is off the table—just open an issue or PR!

---

## Usage & Integration

**1. Basic Installation**  
- Clone the repo:  
  ```bash
  git clone https://github.com/or-mihai-or-gheorghe/MIND-tech-ontology.git
  ```

**2. Taxonomy in Action**  
- See [`skills.py`](./skills.py) for classes like `Taxonomy`, `Skill`, `Framework`, etc.  
- Load the taxonomy and JSON files:
  ```python
  from taxonomy import Taxonomy
  
  taxonomy = Taxonomy()
  taxonomy.load_concepts("./concepts")
  taxonomy.import_from_json("./skills/frameworks_frontend.json")
  # ...and so on
  ```
- Use methods like `taxonomy.get_skill("React.js")` to retrieve skill objects, synonyms, and implied knowledge.  

**3. Extending**  
- Create your own JSON files with new skills or concepts.  
- Or dynamically add skills at runtime with `taxonomy.add_skill_from_dict(...)`.  

---

## License

This project is released under the [MIT License](LICENSE). Feel free to reuse, modify, and distribute it as per the license terms.

---

## Contact & Feedback

- For questions, suggestions, or partnership inquiries, please open an Issue.  
- We’re excited to see how you use and extend this ontology. Let’s build a better way to describe, map, and match tech skills—together!

**Thank you!**  
