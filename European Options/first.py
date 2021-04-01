import qiskit

provider = qiskit.IBMQ.load_account()
backend = provider.backend.ibmq_athens

circ = qiskit.QuantumCircuit(2)
circ.h(0)
circ.cx(0, 1)

circ.draw('mpl')