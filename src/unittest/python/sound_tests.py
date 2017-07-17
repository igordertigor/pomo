import unittest
from unittest import mock

from pomo import sound


class SoundTests(unittest.TestCase):

    @mock.patch('pygame.init')
    def test_initializes_pygame(self, mock_init):

        sound.SoundPlayer('ANY_SOUND')
        mock_init.assert_called_once_with()

    @mock.patch('pygame.init', mock.Mock())
    @mock.patch('pygame.mixer.music.load')
    @mock.patch('pygame.mixer.music.play')
    def test_plays_from_sound_file(self, mock_play, mock_load):
        player = sound.SoundPlayer('ANY_SOUND')
        player.play()
        mock_load.assert_called_once_with('ANY_SOUND')
        mock_play.assert_called_once_with()

    @mock.patch('pygame.init', mock.Mock())
    def test_schedule_schedules_for_later_play(self):
        player = sound.SoundPlayer('ANY_SOUND')
        mock_loop = mock.Mock()
        player.schedule('ANY_TIME', mock_loop)
        mock_loop.call_later.assert_called_once_with('ANY_TIME', player.play)
