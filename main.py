


import python_insertion_sort as p_is
try:
    import cython_insertion_sort as c_is
except ModuleNotFoundError:
    # No Cython module found, compiling now.
    # This is another method to compile Cython programs from within a snippet
    from distutils.core import setup
    from Cython.Build import cythonize

    setup(
        ext_modules= cythonize("cython_insertion_sort.pyx"),
        # build_dir= "build",
        script_args= ['build_ext', "--inplace"]
    )
    import cython_insertion_sort as c_is
from utils import generate_nums, timeit


def main():
    values = generate_nums(n= 10000)

    result1, t1 = timeit(
        c_is.sort, values.copy()
    )

    result2, t2 = timeit(
        p_is.sort, values.copy()
    )

    print(f"Python takes {t2:.4f} seconds")
    print(f"Cython takes {t1:.4f} seconds")
    print(f"Cython is {t2/t1:.2f}x faster!!")
    print(f"Sorted Array is the same:", result1 == result2)


if __name__ == "__main__":
    print()
    main()
    print("Done------------------------------------------\n")
