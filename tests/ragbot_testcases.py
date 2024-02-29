import unittest
from aws_rag_bot.prompt_library import NasaSpokespersonPrompts
from aws_rag_bot.rag_chatbot import RagChatbot, LlmModelTypes
from langchain_core.messages import HumanMessage
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
domain_name = os.getenv("OPENSEARCH_DOMAIN")
question = "what is the Answer to the Ultimate Question of Life, the Universe, and Everything"
context_question = "How many astronauts are going to the moon?"

conv_question1 = "How many astronauts are going to the moon?"
conv_question2 = "What are their names?"


class TestRagbot(unittest.TestCase):
    def test_bedrock_titan(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_TITAN_EXPRESS)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life)
        self.assertIn("42", meaning_of_life)

    def test_bedrock_llama2(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_LLAMA2)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life)
        self.assertIn("42", meaning_of_life)

    def test_bedrock_jurassic(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_JURRASIC2_ULTRA)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life)
        self.assertIn("42", meaning_of_life)

    def test_bedrock_claude_instant(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_CLAUDE_INSTANT)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life)
        self.assertIn("42", meaning_of_life)

    def test_openai_gpt4(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.OPENAI_GPT4)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life.content)
        self.assertIn("42", meaning_of_life.content)

    def test_openai_gpt3(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.OPENAI_GPT35)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life.content)
        self.assertIn("42", meaning_of_life.content)

    def test_google_gemini_pro(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.GOOGLE_GEMINI_PRO)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life.content)
        self.assertIn("42", meaning_of_life.content)

    # Test chatob with basic questions
    def test_chatbot_with_titan(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_TITAN_EXPRESS)
        response = chatbot.ask_question(context_question)
        self.assertIsNotNone(response.content)

    def test_chatbot_with_llama2(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_LLAMA2)
        response = chatbot.ask_question(context_question)
        self.assertIsNotNone(response.content)

    def test_chatbot_with_jurassic(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_JURRASIC2_ULTRA)
        response = chatbot.ask_question(context_question)
        self.assertIsNotNone(response.content)

    def test_chatbot_with_claude_instant(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_CLAUDE_INSTANT)
        response = chatbot.ask_question(context_question)
        self.assertIsNotNone(response.content)

    def test_chatbot_with_openai_gpt4(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.OPENAI_GPT4)
        response = chatbot.ask_question(context_question)
        self.assertIsNotNone(response.content)

    def test_chatbot_with_openai_gpt3(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.OPENAI_GPT35)
        response = chatbot.ask_question(context_question)
        self.assertIsNotNone(response.content)

    def test_chatbot_with_google_gemini_pro(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.GOOGLE_GEMINI_PRO)
        response = chatbot.ask_question(context_question)
        self.assertIsNotNone(response.content)

    def test_chatbot_conversation_with_titan(self):
        chat_history = []
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_TITAN_EXPRESS, prompt_model=NasaSpokespersonPrompts)
        response1 = chatbot.ask_question(conv_question1, chat_history)
        print(response1.content)
        self.assertIsNotNone(response1.content)
        chat_history.extend([HumanMessage(content=conv_question1), response1])
        response2 = chatbot.ask_question(conv_question2, chat_history)
        # print(response2.content)
        self.assertIsNotNone(response2.content)

    def test_chatbot_conversation_with_llama2(self):
        chat_history = []
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_LLAMA2, prompt_model=NasaSpokespersonPrompts)
        response1 = chatbot.ask_question(conv_question1, chat_history)
        print(response1.content)
        self.assertIsNotNone(response1.content)
        chat_history.extend([HumanMessage(content=conv_question1), response1])
        response2 = chatbot.ask_question(conv_question2, chat_history)
        print(response2.content)
        self.assertIsNotNone(response2.content)

    def test_chatbot_conversation_with_jurassic(self):
        chat_history = []
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_JURRASIC2_ULTRA, prompt_model=NasaSpokespersonPrompts)
        response1 = chatbot.ask_question(conv_question1, chat_history)
        print(response1.content)
        self.assertIsNotNone(response1.content)
        chat_history.extend([HumanMessage(content=conv_question1), response1])
        response2 = chatbot.ask_question(conv_question2, chat_history)
        print(response2.content)
        self.assertIsNotNone(response2.content)

    def test_chatbot_conversation_with_claude_instant(self):
        chat_history = []
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_CLAUDE_INSTANT, prompt_model=NasaSpokespersonPrompts)
        response1 = chatbot.ask_question(conv_question1, chat_history)
        print(response1.content)
        self.assertIsNotNone(response1.content)
        chat_history.extend([HumanMessage(content=conv_question1), response1])
        response2 = chatbot.ask_question(conv_question2, chat_history)
        print(response2.content)
        self.assertIsNotNone(response2.content)

    def test_chatbot_conversation_with_openai_gpt4(self):
        chat_history = []
        chatbot = RagChatbot(domain_name, LlmModelTypes.OPENAI_GPT4, prompt_model=NasaSpokespersonPrompts)
        response1 = chatbot.ask_question(conv_question1, chat_history)
        print(response1.content)
        self.assertIsNotNone(response1.content)
        chat_history.extend([HumanMessage(content=conv_question1), response1])
        response2 = chatbot.ask_question(conv_question2, chat_history)
        print(response2.content)
        self.assertIsNotNone(response2.content)

    def test_chatbot_conversation_with_openai_gpt3(self):
        chat_history = []
        chatbot = RagChatbot(domain_name, LlmModelTypes.OPENAI_GPT35, prompt_model=NasaSpokespersonPrompts)
        response1 = chatbot.ask_question(conv_question1, chat_history)
        print(response1.content)
        self.assertIsNotNone(response1.content)
        chat_history.extend([HumanMessage(content=conv_question1), response1])
        response2 = chatbot.ask_question(conv_question2, chat_history)
        print(response2.content)
        self.assertIsNotNone(response2.content)

    def test_chatbot_conversation_with_google_gemini_pro(self):
        chat_history = []
        chatbot = RagChatbot(domain_name, LlmModelTypes.GOOGLE_GEMINI_PRO, prompt_model=NasaSpokespersonPrompts)
        response1 = chatbot.ask_question(conv_question1, chat_history)
        print(response1.content)
        self.assertIsNotNone(response1.content)
        chat_history.extend([HumanMessage(content=conv_question1), response1])
        response2 = chatbot.ask_question(conv_question2, chat_history)
        print(response2.content)
        self.assertIsNotNone(response2.content)