# Minimal Robust Python Speed Decorator ⏱️

A high-precision, minimalist Python decorator for measuring function execution time. It uses only **two core imports** for maximum simplicity and compatibility while ensuring **robustness** by preserving function metadata.

## 🌟 Features

* **Minimal Imports:** Requires only `import time` and `import functools`.
* **Robustness:** Uses `@functools.wraps` to maintain the function's original name (`__name__`) and documentation (`__doc__`).
* **High Precision:** Utilizes `time.perf_counter()` for accurate measurements.
* **Simple Output:** Displays the function name and execution time in seconds.

## ⬇️ Installation

Simply copy the `speed_calc_decorator` function from `speed_decorator.py` into your project, or save it as a module and import it.

## 💡 Usage

### Import the Decorator

```python
from speed_decorator import speed_calc_decorator
