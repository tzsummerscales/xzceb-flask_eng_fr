import unittest
import translator

class TestTranslator(unittest.TestCase):
    
    def test_englishToFrench(self):
        self.assertNotEqual(translator.english_to_french('None'), '')
        self.assertNotEqual(translator.english_to_french(0), 0)
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertEqual(translator.english_to_french('I love you'), "Je t'aime")

    def test_frenchToEnglish(self):
        self.assertNotEqual(translator.french_to_english('None'), '')
        self.assertNotEqual(translator.french_to_english(0), 0)
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertEqual(translator.french_to_english("Je t'aime"), 'I love you')


if __name__ == '__main__':
    unittest.main()

