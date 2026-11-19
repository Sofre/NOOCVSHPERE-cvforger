from .base import BaseContext

class TaskContext(self,content:dict):
    
    def __init__(self,content:dict):
        super().__init__(content)

    def build(self) -> dict:

        # validate first
        
        if not self.validate():
            raise ValueError("Invalid content")

        return{
            "type" : "Tasks"
            "content" : self.to_dict()
        }

# Tasks - Using identifers to map out each task per role// Tasks have Objectives, inputs and expected outputs 
tasks = TaskContext({
    {
        # Chatbot 
    "understand_user_request": {
        "task_id": "understand_user_request",
        "role_id": "nosphere_assistant",
        "objective": (
            "Interpret the user's message and identify "
            "their intended career-related request."
        ),
        "inputs": [
            "user_message",
            "conversation_history"
        ],
        "expected_output": "structured_user_intent"
    },
        # Chatbot
    "identify_workflow": {
        "task_id": "identify_workflow",
        "role_id": "nosphere_assistant",
        "objective": (
            "Determine which Nosphere workflow and specialized "
            "agents are required to fulfill the user's request."
        ),
        "inputs": [
            "user_intent",
            "conversation_history"
        ],
        "expected_output": "workflow_selection"
    },
        # Chatbot
    "collect_user_information": {
        "task_id": "collect_user_information",
        "role_id": "nosphere_assistant",
        "objective": (
            "Identify missing information and request "
            "necessary details from the user."
        ),
        "inputs": [
            "user_intent",
            "available_candidate_information"
        ],
        "expected_output": "information_requirements"
    },
        # Chatbot
    "prepare_delegation": {
        "task_id": "prepare_delegation",
        "role_id": "nosphere_assistant",
        "objective": (
            "Determine the tasks, agents, and required inputs "
            "needed to fulfill the user's request."
        ),
        "inputs": [
            "workflow_selection",
            "available_context"
        ],
        "expected_output": "delegation_plan"
    },
        # Chatbot
    "present_results": {
        "task_id": "present_results",
        "role_id": "nosphere_assistant",
        "objective": (
            "Present specialized agent results to the user "
            "in a clear and understandable format."
        ),
        "inputs": [
            "agent_results",
            "conversation_history"
        ],
        "expected_output": "user_facing_response"
    },
        # Chatbot
    "manage_follow_up": {
        "task_id": "manage_follow_up",
        "role_id": "nosphere_assistant",
        "objective": (
            "Interpret follow-up requests and determine "
            "the appropriate next action based on previous results."
        ),
        "inputs": [
            "user_message",
            "conversation_history",
            "previous_workflow_results"
        ],
        "expected_output": "next_action"
    }

}
        # Job Search Agent 
    "search_jobs": {
        "task_id": "search_jobs",
        "role_id": "job_research",
        "objective": "Find job opportunities matching candidate preferences.",
        "inputs": [
            "job_title",
            "location",
            "employment_type",
            "preferred_technologies"
        ],
        "expected_output": "structured_job_listings"
    },
          # Job Search Agent 
    "analyze_job_listing": {
        "task_id": "analyze_job_listing",
        "role_id": "job_research",
        "objective": "Extract structured information from a job listing.",
        "inputs": [
            "job_listing"
        ],
        "expected_output": "job_profile"
    },
              # Job Search Agent 
    "filter_job_listings": {
        "task_id": "filter_job_listings",
        "role_id": "job_research",
        "objective": "Filter job listings according to candidate preferences.",
        "inputs": [
            "job_listings",
            "candidate_preferences"
        ],
        "expected_output": "filtered_job_listings"
    },

              # CV analysis Agent 
        "analyze_candidate": {
        "task_id": "analyze_candidate",
        "role_id": "career_analysis",
        "objective": "Analyze and structure the candidate's professional qualifications.",
        "inputs": [
            "candidate_cv"
        ],
        "expected_output": "candidate_profile"
    },
          # CV analysis Agent 
    "compare_candidate": {
        "task_id": "compare_candidate",
        "role_id": "career_analysis",
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
        "role_id": "career_analysis",
        "objective": "Identify missing or insufficient candidate qualifications.",
        "inputs": [
            "candidate_profile",
            "job_profile"
        ],
        "expected_output": "skill_gap_report"
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
