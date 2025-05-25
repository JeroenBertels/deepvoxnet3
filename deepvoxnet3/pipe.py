

class Pipe:
    def __init__(self, input_pipe=None, pipe_fn=None, pipe_fn_params=None):
        self.input_pipe = input_pipe
        self.pipe_fn = pipe_fn
        self.pipe_fn_params = pipe_fn_params
        self._pipe_output = None

    def eval(self):
        if self._pipe_output is not None:
            return self._pipe_output

        else:
            return self.pipe()
    
    def pipe(self):
        if self.pipe_fn is None:
            self._pipe_output = None
        
        else:
            self._pipe_output = self.pipe_fn(self.input_pipe.pipe(), **self.pipe_fn_params)

        return self._pipe_output
