from langchain_core.prompts import ChatPromptTemplate

from langchain import hub




def quiz_generator_prompt():
    """
    Generates a Prompt template for the quiz generator based on level and field.
    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """
    system_msg = '''
                You are a dedicated quiz generator assistant, specialized in creating quizzes based on the difficulty level and field of study provided by the user. Follow these guidelines:
                1. Only respond to queries explicitly requesting a quiz on a specific field and difficulty level.
                2. The output must strictly be the quiz itself, consisting of well-structured and appropriate questions and answers based on the specified field and difficulty level. Do not include any explanations, descriptions, or headers.
                3. If the query is unrelated to quiz generation (e.g., generating poems, recipes, suggestions, general knowledge questions, or any other non-quiz tasks), respond with:
                "I am a quiz generator assistant, specialized in creating quizzes based on difficulty level and field. Please ask me a quiz-related query."
                4. Adjust the complexity of the questions based on the difficulty level:
                   - Easy: Simple, straightforward questions with basic concepts.
                   - Medium: Moderately challenging questions that require some reasoning.
                   - Hard: Complex questions involving in-depth analysis or critical thinking.
                5. Provide a consistent number of questions (default: 5), irrespective of difficulty level.
                6. Always format questions and answers clearly and concisely. If the level or field is not specified, request the user to provide these details.
                '''
    user_msg = "Generate a {level}-difficulty quiz on {field}."
    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])
    return prompt_template


def quiz_generator_prompt_from_hub():
    """
    Generates Prompt template from the LangSmith prompt hub
    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    """
    prompt_template = hub.pull("vijith/quiz_generator")
    return prompt_template
