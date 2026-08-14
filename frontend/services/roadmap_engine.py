from typing import Any


def generate_roadmap(profile: dict[str, Any]) -> dict[str, Any]:
    """
    Generate a personalized roadmap from a developer profile.

    Currently uses a rule-based engine.
    Later this function will call an LLM service.
    """

    career_goal = profile.get(
        "career_goal",
        "Software Engineer",
    )

    level = profile.get(
        "experience_level",
        "Beginner",
    )

    skills = profile.get(
        "skills",
        [],
    )

    target = profile.get(
        "target",
        "Job",
    )

    timeline = profile.get(
        "timeline",
        "6 months",
    )

    daily_time = profile.get(
        "daily_time",
        "2–4 hours/day",
    )

    # ------------------------------------------------------------
    # Determine roadmap type
    # ------------------------------------------------------------

    goal = career_goal.lower()

    if (
        "ai" in goal
        or "machine learning" in goal
        or "ml" in goal
        or "genai" in goal
    ):
        roadmap_type = "ai"

    elif (
        "full-stack" in goal
        or "full stack" in goal
        or "backend" in goal
        or "frontend" in goal
        or "software" in goal
    ):
        roadmap_type = "software"

    elif "data" in goal:

        roadmap_type = "data"

    else:

        roadmap_type = "general"

    # ------------------------------------------------------------
    # Build phases
    # ------------------------------------------------------------

    if roadmap_type == "ai":

        phases = build_ai_roadmap(
            level,
            skills,
        )

    elif roadmap_type == "software":

        phases = build_software_roadmap(
            level,
            skills,
        )

    elif roadmap_type == "data":

        phases = build_data_roadmap(
            level,
            skills,
        )

    else:

        phases = build_general_roadmap(
            level,
            skills,
        )

    # ------------------------------------------------------------
    # Return structured roadmap
    # ------------------------------------------------------------

    return {
        "title": f"Roadmap to {career_goal}",

        "career_goal": career_goal,

        "current_level": level,

        "target": target,

        "timeline": timeline,

        "daily_time": daily_time,

        "progress": 0,

        "phases": phases,
    }


# =================================================================
# AI / ML ROADMAP
# =================================================================

def build_ai_roadmap(
    level: str,
    skills: list[str],
) -> list[dict]:

    skills_lower = {
        skill.lower()
        for skill in skills
    }

    phases = []


    # -------------------------------------------------------------
    # Python foundation
    # -------------------------------------------------------------

    python_known = "python" in skills_lower

    if python_known and level != "Beginner":

        phases.append(
            {
                "id": "ai-01",

                "title": "AI Engineering Foundations",

                "description":
                    "Strengthen the engineering fundamentals required for AI development.",

                "skills": [
                    "Advanced Python",
                    "Git",
                    "APIs",
                    "SQL",
                ],

                "topics": [
                    "Python modules",
                    "OOP",
                    "Error handling",
                    "REST APIs",
                    "Database fundamentals",
                ],

                "project":
                    "AI Developer Data Platform",

                "status":
                    "current",
            }
        )

    else:

        phases.append(
            {
                "id": "ai-01",

                "title": "Programming Foundations",

                "description":
                    "Build the programming foundation required before moving into AI.",

                "skills": [
                    "Python",
                    "Git",
                    "SQL",
                    "Problem Solving",
                ],

                "topics": [
                    "Python fundamentals",
                    "Functions",
                    "OOP",
                    "Git",
                    "SQL basics",
                ],

                "project":
                    "Developer Productivity Analyzer",

                "status":
                    "current",
            }
        )


    # -------------------------------------------------------------
    # Machine Learning
    # -------------------------------------------------------------

    ml_known = (
        "machine learning" in skills_lower
    )

    phases.append(
        {
            "id": "ai-02",

            "title": "Machine Learning",

            "description":
                "Learn how to train, evaluate and deploy classical machine learning models.",

            "skills": [
                "NumPy",
                "Pandas",
                "Statistics",
                "Scikit-learn",
            ],

            "topics": [
                "Data preprocessing",
                "Feature engineering",
                "Regression",
                "Classification",
                "Model evaluation",
                "Cross-validation",
            ],

            "project":
                "Developer Skill Prediction System",

            "status":
                "upcoming"
                if not ml_known
                else "current",
        }
    )


    # -------------------------------------------------------------
    # Deep Learning
    # -------------------------------------------------------------

    phases.append(
        {
            "id": "ai-03",

            "title": "Deep Learning",

            "description":
                "Move from classical machine learning to neural-network based systems.",

            "skills": [
                "Neural Networks",
                "PyTorch",
                "CNNs",
                "Model Training",
            ],

            "topics": [
                "Perceptron",
                "Backpropagation",
                "Optimization",
                "CNN",
                "Transfer learning",
            ],

            "project":
                "Intelligent Developer Classification System",

            "status":
                "upcoming",
        }
    )


    # -------------------------------------------------------------
    # GenAI
    # -------------------------------------------------------------

    phases.append(
        {
            "id": "ai-04",

            "title": "Generative AI",

            "description":
                "Build modern AI applications using large language models.",

            "skills": [
                "LLMs",
                "Prompt Engineering",
                "Embeddings",
                "Vector Databases",
                "RAG",
            ],

            "topics": [
                "LLM fundamentals",
                "Prompt design",
                "Embeddings",
                "Semantic search",
                "RAG pipelines",
            ],

            "project":
                "AI Developer Career Assistant",

            "status":
                "upcoming",
        }
    )


    # -------------------------------------------------------------
    # AI Agents
    # -------------------------------------------------------------

    phases.append(
        {
            "id": "ai-05",

            "title": "AI Agents",

            "description":
                "Build AI systems capable of using tools and completing multi-step tasks.",

            "skills": [
                "Tool Calling",
                "Agents",
                "Workflows",
                "Memory",
            ],

            "topics": [
                "Tool use",
                "Agent loops",
                "Planning",
                "Memory",
                "Multi-step workflows",
            ],

            "project":
                "Autonomous Developer Mentor",

            "status":
                "upcoming",
        }
    )


    # -------------------------------------------------------------
    # Production AI
    # -------------------------------------------------------------

    phases.append(
        {
            "id": "ai-06",

            "title": "Production AI",

            "description":
                "Learn how to turn AI prototypes into reliable production applications.",

            "skills": [
                "FastAPI",
                "Docker",
                "Cloud",
                "Monitoring",
            ],

            "topics": [
                "Model serving",
                "API architecture",
                "Docker",
                "Deployment",
                "Monitoring",
            ],

            "project":
                "Production AI Developer Platform",

            "status":
                "upcoming",
        }
    )

    return phases


# =================================================================
# SOFTWARE ENGINEERING ROADMAP
# =================================================================

def build_software_roadmap(
    level: str,
    skills: list[str],
) -> list[dict]:

    skills_lower = {
        skill.lower()
        for skill in skills
    }


    return [

        {
            "id": "se-01",

            "title": "Programming & DSA",

            "description":
                "Build strong programming and problem-solving fundamentals.",

            "skills": [
                "Programming",
                "DSA",
                "Git",
                "Problem Solving",
            ],

            "topics": [
                "Data structures",
                "Algorithms",
                "Complexity",
                "Problem solving",
            ],

            "project":
                "Developer Productivity Toolkit",

            "status":
                "current",
        },

        {
            "id": "se-02",

            "title": "Backend Engineering",

            "description":
                "Learn how production backend applications are designed.",

            "skills": [
                "REST APIs",
                "FastAPI",
                "PostgreSQL",
                "Authentication",
            ],

            "topics": [
                "API design",
                "Authentication",
                "Databases",
                "Validation",
            ],

            "project":
                "Developer Collaboration Platform",

            "status":
                "upcoming",
        },

        {
            "id": "se-03",

            "title": "Frontend Engineering",

            "description":
                "Build modern interactive interfaces and connect them to APIs.",

            "skills": [
                "JavaScript",
                "React",
                "State Management",
                "API Integration",
            ],

            "topics": [
                "Modern JavaScript",
                "React",
                "Components",
                "API integration",
            ],

            "project":
                "Developer Analytics Dashboard",

            "status":
                "upcoming",
        },

        {
            "id": "se-04",

            "title": "System Design",

            "description":
                "Understand how scalable software systems are designed.",

            "skills": [
                "System Design",
                "Caching",
                "Databases",
                "Queues",
            ],

            "topics": [
                "Scalability",
                "Caching",
                "Load balancing",
                "Database design",
            ],

            "project":
                "Scalable Developer Platform",

            "status":
                "upcoming",
        },

        {
            "id": "se-05",

            "title": "Production Engineering",

            "description":
                "Deploy and operate applications in production.",

            "skills": [
                "Docker",
                "Cloud",
                "CI/CD",
                "Monitoring",
            ],

            "topics": [
                "Containers",
                "CI/CD",
                "Cloud deployment",
                "Monitoring",
            ],

            "project":
                "Production-Ready SaaS Platform",

            "status":
                "upcoming",
        },

    ]


# =================================================================
# DATA SCIENCE ROADMAP
# =================================================================

def build_data_roadmap(
    level: str,
    skills: list[str],
) -> list[dict]:

    return [

        {
            "id": "ds-01",

            "title": "Data Foundations",

            "description":
                "Build the foundations required for working with data.",

            "skills": [
                "Python",
                "SQL",
                "Statistics",
                "Git",
            ],

            "topics": [
                "Python",
                "SQL",
                "Descriptive statistics",
                "Data cleaning",
            ],

            "project":
                "Developer Analytics Platform",

            "status":
                "current",
        },

        {
            "id": "ds-02",

            "title": "Data Analysis",

            "description":
                "Learn how to transform raw data into useful insights.",

            "skills": [
                "Pandas",
                "NumPy",
                "Matplotlib",
                "EDA",
            ],

            "topics": [
                "Data manipulation",
                "EDA",
                "Visualization",
                "Feature analysis",
            ],

            "project":
                "Developer Career Analytics System",

            "status":
                "upcoming",
        },

        {
            "id": "ds-03",

            "title": "Machine Learning",

            "description":
                "Use machine learning to build predictive systems.",

            "skills": [
                "Scikit-learn",
                "Regression",
                "Classification",
                "Evaluation",
            ],

            "topics": [
                "Supervised learning",
                "Unsupervised learning",
                "Feature engineering",
                "Evaluation",
            ],

            "project":
                "Career Outcome Prediction System",

            "status":
                "upcoming",
        },

        {
            "id": "ds-04",

            "title": "Production Data Systems",

            "description":
                "Learn how data products are deployed and maintained.",

            "skills": [
                "FastAPI",
                "Docker",
                "Cloud",
                "Data Pipelines",
            ],

            "topics": [
                "APIs",
                "Pipelines",
                "Deployment",
                "Monitoring",
            ],

            "project":
                "Production Data Intelligence Platform",

            "status":
                "upcoming",
        },

    ]


# =================================================================
# GENERAL ROADMAP
# =================================================================

def build_general_roadmap(
    level: str,
    skills: list[str],
) -> list[dict]:

    return [

        {
            "id": "gen-01",

            "title": "Foundations",

            "description":
                "Build strong programming and development fundamentals.",

            "skills": [
                "Programming",
                "Git",
                "SQL",
                "Problem Solving",
            ],

            "topics": [
                "Programming fundamentals",
                "Git",
                "SQL",
                "Problem solving",
            ],

            "project":
                "Developer Utility Platform",

            "status":
                "current",
        },

        {
            "id": "gen-02",

            "title": "Application Development",

            "description":
                "Learn how real-world applications are built.",

            "skills": [
                "APIs",
                "Databases",
                "Backend",
                "Testing",
            ],

            "topics": [
                "REST APIs",
                "Databases",
                "Authentication",
                "Testing",
            ],

            "project":
                "Developer Management Platform",

            "status":
                "upcoming",
        },

        {
            "id": "gen-03",

            "title": "Advanced Engineering",

            "description":
                "Move toward production-quality engineering.",

            "skills": [
                "Architecture",
                "System Design",
                "Docker",
                "Cloud",
            ],

            "topics": [
                "Architecture",
                "Scalability",
                "Containers",
                "Deployment",
            ],

            "project":
                "Production Developer Application",

            "status":
                "upcoming",
        },

    ]