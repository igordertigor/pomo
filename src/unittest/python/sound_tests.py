import unittest
from unittest import mock

import subprocess

from pomo import sound


class SoundTests(unittest.TestCase):

    @mock.patch('subprocess.run')
    @mock.patch('pygame.init')
    def test_initializes_pygame_if_no_mpg321(self, mock_init, mock_run):
        mock_run().returncode = 1

        sound.SoundPlayer('ANY_SOUND')
        mock_init.assert_called_once_with()

    @mock.patch('pygame.init', mock.Mock())
    @mock.patch('subprocess.run')
    @mock.patch('pygame.mixer.music.load')
    @mock.patch('pygame.mixer.music.play')
    def test_plays_from_sound_file_if_no_mpg321(self,
                                                mock_play,
                                                mock_load,
                                                mock_run):

        mock_run().returncode = 1
        player = sound.SoundPlayer('ANY_SOUND')
        player.play()
        mock_load.assert_called_once_with('ANY_SOUND')
        mock_play.assert_called_once_with()

    @mock.patch('pygame.init', mock.Mock())
    @mock.patch('subprocess.run')
    def test_schedule_schedules_for_later_play(self, mock_run):
        mock_run().returncode = 1
        player = sound.SoundPlayer('ANY_SOUND')
        mock_loop = mock.Mock()
        player.schedule('ANY_TIME', mock_loop)
        mock_loop.call_later.assert_called_once_with('ANY_TIME', player.play)

    @mock.patch('subprocess.run')
    def test_uses_run_call_if_mpg321(self, mock_run):
        mock_run.return_value.returncode = 0
        player = sound.SoundPlayer('ANY_SOUND')
        player.play()
        self.assertSequenceEqual(
            mock_run.mock_calls,
            [mock.call(['which', 'mpg321'], stderr=subprocess.PIPE),
             mock.call(['mpg321', 'ANY_SOUND'], stderr=subprocess.PIPE)])
