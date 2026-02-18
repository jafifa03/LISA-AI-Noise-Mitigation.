import importlib
import json
import sys

modules = [
    'numpy',
    'torch',
    'torch.nn',
    'torch.optim',
    'torch.utils.tensorboard',
    'gymnasium',
    'gymnasium.spaces',
    'matplotlib',
    'matplotlib.pyplot',
    'scipy',
    'scipy.signal',
    'scipy.fft',
    'logging',
    'typing',
    'json',
    'dataclasses',
    'collections',
    'collections.deque'
]

results = {}
for name in modules:
    try:
        mod = importlib.import_module(name)
        version = getattr(mod, '__version__', None)
        if version is None:
            # try to get top-level package version via importlib.metadata if available
            try:
                import importlib.metadata as ilm
                top = name.split('.')[0]
                version = ilm.version(top)
            except Exception:
                version = None
        results[name] = {'installed': True, 'version': version}
    except Exception as e:
        results[name] = {'installed': False, 'error': str(e)}

# human-readable summary
for k, v in results.items():
    if v['installed']:
        ver = v['version'] if v['version'] is not None else 'unknown'
        print(f"OK: {k} — version: {ver}")
    else:
        print(f"MISSING: {k} — error: {v['error']}")

# also output JSON to stdout for programmatic use
print('\nJSON_OUTPUT_START')
print(json.dumps(results, indent=2))
print('JSON_OUTPUT_END')
