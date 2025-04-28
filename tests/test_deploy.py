import sys
import unittest
from versioner.commands.deploy import deploy
from versioner.utils.version_manager import increment_version, read_version  # Replace with the actual function name

class TestDeployCommand(unittest.TestCase):
    '''Test the deploy command for expected behavior.'''
    def test_deploy_success(self):
        """Test the deploy function for expected behavior."""
        # Define args for -m and --message
        args = ['-m', 'test(deploy): Test commit message']
        
        # Simulate command line arguments
        sys.argv = ['deploy.py'] + args
        # Check if the result is as expected
        success_version = increment_version("minor", write=False)
        deploy()
        self.assertEqual(success_version,read_version())

    def test_deploy_failure(self):
        '''Test the deploy function for failure case.'''
        sys.argv = ['deploy.py', '-m', 'invalid commit message']
        old_version = read_version()
        deploy()
        self.assertEqual(old_version, read_version())

    def test_deploy_invalid_args(self):
        """Test the deploy function with invalid arguments."""
        sys.argv = ['deploy.py', '--invalid-arg']
        old_version = read_version()
        deploy()
        self.assertEqual(old_version, read_version())
    
    
if __name__ == '__main__':
    unittest.main()