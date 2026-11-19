from .base import BaseContext

class TaskContext(BaseContext):
    def build(self) -> dict:
        if not self.validate():
            raise ValueError("Invalid task context")
        return {
            "type": "tasks",
            "content": self.to_dict(),
        }

# Tasks map each task to a role, its inputs, objective, and expected output.
tasks = TaskContext({
    
        # Chatbot  - understand user request
    "understand_user_request": {
        "task_id": "understand_user_request",
        "role_id": "noocvsphere_assistant",
        "objective": (
            "Interpret the user's message in the context "
            "of the ongoing conversation and identify "
            "the intended request, goals and constraints."
        ),
        "inputs": [
            "user_message",
            "conversation_history",
            "short_term_memory",
            "long_term_memory"
        ],
        "expected_output": "structured_user_intent"
    },
        # Chatbot - identify which workflow he wants and agents to be activated
    "identify_workflow": {
        "task_id": "identify_workflow",
        "role_id": "noocvsphere_assistant",
        "objective": (
            "Determine which workflow and specialized agents "
            "are required to fulfill the user's request."
        ),
        "inputs": [
            "user_intent",
            "conversation_history",
            "available_workflows",
            "available_agents"
        ],
        "expected_output": "workflow_selection"
    },
        # Chatbot - collect the information from the user 
    "collect_user_information": {
        "task_id": "collect_user_information",
        "role_id": "noocvsphere_assistant",
        "objective": (
             "Identify missing or insufficient information "
            "required to execute the selected workflow and "
            "request clarification when necessary."
        ),
        "inputs": [
            "structured_user_intent",
            "workflow_selection",
            "available_user_information"
        ],
        "expected_output": "information_requirements"
    },
        # Chatbot - prepare to deleagte instructions to the agents
    "prepare_delegation": {
        "task_id": "prepare_delegation",
        "role_id": "noocvsphere_assistant",
        "objective": (
            "Prepare the delegation instructions, required "
            "inputs, relevant context and expected outputs "
            "for the selected specialized agents."
        ),
        "inputs": [
            "workflow_selection",
            "structured_user_intent",
            "available_context",
            "information_requirements"
        ],
        "expected_output": "delegation_plan"
    },
        # Chatbot - validate and present results
    "present_results": {
        "task_id": "present_results",
        "role_id": "noocvsphere_assistant",
        "objective": (
            "Validate specialized agent results against "
            "the original request and present the verified "
            "results to the user."
        ),
        "inputs": [
            "agent_results",
            "structured_user_intent",
            "conversation_history"
        ],
        "expected_output": "user_facing_response"
    },
        # Chatbot - manage a followup request 
    "manage_follow_up": {
        "task_id": "manage_follow_up",
        "role_id": "noocvsphere_assistant",
        "objective": (
            "Interpret follow-up requests using the existing "
            "conversation state and previous workflow results "
            "to determine the appropriate next action."
        ),
        "inputs": [
            "user_message",
            "conversation_history",
            "short_term_memory",
            "previous_workflow_results"
        ],
        "expected_output": "next_action"
    },

        # Job Search Agent - Search Jobs 
    "search_jobs": {
    "task_id": "search_jobs",
    "role_id": "job_researcher",
    "objective": "Discover job opportunities using the candidate's search criteria.",
    "inputs": [
        "job_title",
        "location",
        "employment_type",
        "preferred_technologies",
        "salary_expectations",
        "remote_preference"
    ],
    "expected_output": "raw_job_listings"
},
          # Job Search Agent - Analyzie lisitng
    "analyze_job_listing": {
        "task_id": "analyze_job_listing",
        "role_id": "job_researcher",
        "objective": "Extract structured information from a job listing.",
        "inputs": [
            "job_listing"
        ],
        "expected_output": "job_profile"
    },
              # Job Search Agent  - filter job by user pref
    "filter_job_listings": {
        "task_id": "filter_job_listings",
        "role_id": "job_researcher",
        "objective": "Filter job listings according to candidate preferences.",
        "inputs": [
            "job_listings",
            "candidate_preferences"
        ],
        "expected_output": "filtered_job_listings"
    },

              # CV analysis Agent - anlyize the cv as actuall facts
        "analyze_candidate": {
        "task_id": "analyze_candidate",
        "role_id": "career_researcher",
        "objective": "Analyze and structure the candidate's professional qualifications.",
        "inputs": [
            "candidate_cv"
        ],
        "expected_output": "candidate_profile"
    },
          # CV analysis Agent - compare candidate qualifactions against job reqirments
    "compare_candidate": {
        "task_id": "compare_candidate",
        "role_id": "career_researcher",
        "objective": "Compare candidate qualifications against job requirements.",
        "inputs": [
            "candidate_profile",
            "job_profile"
        ],
        "expected_output": "compatibility_analysis"
    },
          # CV analysis Agent 
    "identify_skill_gaps": {
        "task_id": "identify_skill_gaps",
        "role_id": "career_researcher",
        "objective": "Identify missing or insufficient candidate qualifications.",
        "inputs": [
            "candidate_profile",
            "job_profile"
        ],
        "expected_output": "skill_gap_report"
    },
    # CV analysis ATS Score
    "evaluate_ats_compatibility": {
    "task_id": "evaluate_ats_compatibility",
    "role_id": "career_researcher",
    "objective": (
        "Evaluate the candidate's CV against the job listing "
        "based on keyword relevance, required skills, "
        "qualifications and ATS readability."
    ),
    "inputs": [
        "candidate_profile",
        "job_profile",
        "candidate_cv"
    ],
    "expected_output": "ats_compatibility_report"
},

        # CV Builder Agent 
        "generate_cv": {
        "task_id": "generate_cv",
        "role_id": "cv_builder",
        "objective": "Generate a tailored CV for a target position.",
        "inputs": [
            "candidate_profile",
            "job_profile",
            "compatibility_analysis"
        ],
        "expected_output": "structured_cv"
    },
        # CV builder Agent 
    "generate_cover_letter": {
        "task_id": "generate_cover_letter",
        "role_id": "cv_builder",
        "objective": "Generate a tailored professional cover letter.",
        "inputs": [
            "candidate_profile",
            "job_profile",
            "compatibility_analysis"
        ],
        "expected_output": "cover_letter"
    },
        # CV builder Agent 
    "improve_cv": {
        "task_id": "improve_cv",
        "role_id": "cv_builder",
        "objective": "Improve existing CV content while preserving factual accuracy.",
        "inputs": [
            "candidate_profile",
            "improvement_instructions"
        ],
        "expected_output": "improved_cv"
    }

})

