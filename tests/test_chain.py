import unittest
from chain_llm.chain import Chain


class TestChain(unittest.TestCase):
    def test_chain_init(self):
        chain = Chain()
        self.assertIsInstance(chain, Chain, "Object is not an instance of CHain")


if __name__ == "__main__":
    unittest.main()
