from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        #print(result)
        #result_1 = emotion_detector('I am glad this happened')
        self.assertIsNotNone(result["joy"])

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        #print(result)
        self.assertIsNotNone(result["anger"])

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        #print(result)
        self.assertIsNotNone(result["disgust"])

    def test_sadness(self):
        result = emotion_detector("I am sad.")
        self.assertIsNotNone(result["sadness"])

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        #print(result)
        self.assertIsNotNone(result["fear"])

if __name__ == "__main__":
    unittest.main()    
    