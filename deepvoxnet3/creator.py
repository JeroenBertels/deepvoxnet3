import random
from typing import Any, Callable, List, Optional, Tuple, Union


class Pipe:
    def __init__(
        self,
        input_data: Union["Pipe", Any],
        transform_fn: Callable[[Any, dict, random.Random], Any],
        params: dict,
        rng: random.Random
    ):
        self.input_data = input_data
        self.transform_fn = transform_fn
        self.params = params
        self.rng = rng

    def eval(self) -> Any:
        input_val = self.input_data.eval() if isinstance(self.input_data, Pipe) else self.input_data
        return self.transform_fn(input_val, self.params, self.rng)


class Creator:
    def __init__(
        self,
        params: Optional[dict] = None,
        reference_pipes: Optional[List[Pipe]] = None
    ):
        self.params = params or {}
        self.reference_pipes = reference_pipes or []
        self.rng = self._initialize_rng()
        self.created_pipes: List[Pipe] = []

    def __call__(self, *inputs: Union[Pipe, Any]) -> Union[Pipe, Tuple[Pipe, ...]]:
        outputs = tuple(self._create_pipe(inp) for inp in inputs)
        return outputs[0] if len(outputs) == 1 else outputs

    def _create_pipe(self, input_data: Union[Pipe, Any]) -> Pipe:
        pipe = Pipe(
            input_data=input_data,
            transform_fn=self._transform_fn,
            params=self.params,
            rng=self.rng
        )
        self.created_pipes.append(pipe)
        return pipe

    def _initialize_rng(self) -> random.Random:
        # You can customize how the RNG is seeded, e.g., from reference pipes
        return random.Random(42)

    def _transform_fn(self, input_val: Any, params: dict, rng: random.Random) -> Any:
        """
        Override this method in subclasses to define actual behavior.
        """
        raise NotImplementedError("Each Creator must implement its own transform function.")
