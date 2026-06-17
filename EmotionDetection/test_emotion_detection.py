from emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        joy_test = emotion_detector("I am glad this happened")["dominant_emotion"]
        anger_test = emotion_detector("I am really mad about this")["dominant_emotion"]
        disgust_test = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        sadness_test = emotion_detector("I am so sad about this")["dominant_emotion"]
        fear_test = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]

        self.assertEqual(joy_test, "joy")
        self.assertEqual(anger_test, "anger")
        self.assertEqual(disgust_test, "disgust")
        self.assertEqual(sadness_test, "sadness")
        self.assertEqual(fear_test, "fear")

unittest.main()