import unittest
from unittest.mock import patch  # noqa
from chain_llm.chain import Chain
from chain_llm.llm_generation import LLMGeneration


class TestChain(unittest.TestCase):
    def test_chain_init(self):
        chain = Chain([LLMGeneration("hello")])
        self.assertIsInstance(chain, Chain, "Object is not an instance of CHain")

    @patch("chain_llm.llm_generation.LLMGeneration.request_generation")
    def test_chain(self, mock_request_generation):
        # Configure the mock behavior
        mock_request_generation.return_value = {"choices": [{"text": "ducks."}]}

        # Optionally, assert that the method was called with the expected arguments
        # mock_my_method.assert_called_once_with()

        links = [
            LLMGeneration("Tell me a joke."),
            LLMGeneration("Edit this joke to be longer."),
        ]
        chain = Chain(links)
        resultstr = chain.run()
        self.assertEqual(resultstr, "ducks.")
        # self.assertEqual(result, "Mocked result")


if __name__ == "__main__":
    unittest.main()
