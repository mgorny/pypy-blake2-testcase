#include <assert.h>
#include <Python.h>

static unsigned char expected_i = '0';

static PyObject* testmod_test(PyObject* self, PyObject* args)
{
	PyObject* obj;
	Py_buffer bp;

	if (!PyArg_ParseTuple(args, "O", &obj))
		return NULL;

	assert(obj);

	if (PyObject_GetBuffer(obj, &bp, PyBUF_SIMPLE) == -1)
		return NULL;

	for (size_t i = 0; i < bp.len; ++i)
	{
		if (((unsigned char*)bp.buf)[i] == expected_i)
		{
			if (++expected_i >= '8')
				expected_i = '0';
		}
		else
		{
			PyErr_Format(PyExc_ValueError, "mismatch: 0x%x [%x %x %x %x...] instead of 0x%x on pos=%d (got len=%d)",
					((unsigned char*)bp.buf)[i],
					((unsigned char*)bp.buf)[i+1],
					((unsigned char*)bp.buf)[i+2],
					((unsigned char*)bp.buf)[i+3],
					((unsigned char*)bp.buf)[i+4],
					expected_i, i, bp.len);
			PyBuffer_Release(&bp);
			return NULL;
		}
	}

	PyBuffer_Release(&bp);
	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef TestModMethods[] = {
	{"test", testmod_test, METH_VARARGS, "test it"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC inittestmod()
{
	Py_InitModule("testmod", TestModMethods);
}
