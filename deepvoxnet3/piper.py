from deepvoxnet3.pipe import Pipe


class Piper:
    def __init__(self, reference_pipes=None, **piper_params):
        self.reference_pipes = reference_pipes or []
        self.piper_params = piper_params
        self._pipes = []
        self._piper_fn_params = {}

    def __call__(self, *input_pipes):
        if input_pipes:
            new_pipes = []
            for input_pipe in input_pipes:
                new_pipes.append(self._create_pipe(input_pipe))

            self._pipes.extend(new_pipes)
            return new_pipes[0] if len(new_pipes) == 1 else new_pipes

    def _create_pipe(self, input_pipe):
        return Pipe(input_pipe=input_pipe, pipe_fn=self._piper_fn, pipe_fn_params=self._piper_fn_params)

    def _piper_fn(self, input_val, **kwargs):
        raise NotImplementedError
