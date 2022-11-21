
# upgrade pip
pip install --upgrade pip

# install CPU version
pip install --upgrade "jax[cpu]"

# install GPU
pip install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

