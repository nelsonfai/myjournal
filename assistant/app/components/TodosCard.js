"use client";

import { useState } from 'react';
import { FaTrash, FaCheck, FaPlus, FaSpinner } from 'react-icons/fa';
import useFirebase from "@/lib/useFirebase";

const TodosCard = () => {
  const { todos, loading, addTodo, deleteTodo, updateTodo } = useFirebase();
  const [newTodo, setNewTodo] = useState("");

  if (loading) return <div className="flex justify-center items-center h-32"><FaSpinner className="animate-spin text-gray-700 text-2xl" /></div>;

  return (
    <div className="todos-container p-6 bg-white shadow-lg rounded-lg max-w-sm mx-auto md:max-w-md border border-gray-300">
      <h2 className="text-2xl font-bold mb-4 text-black">To-Do List</h2>
      {todos.length > 0 ? (
        <ul className="todos-list max-h-96 overflow-y-auto md:max-h-[24rem]">
          {todos.map((todo) => (
            <li key={todo.id} className="mb-2">
              <div className="flex justify-between items-center p-2 border rounded-lg shadow-sm">
                <div>
                  <p className="font-semibold text-black">{todo.item}</p>
                  <small className="text-gray-500">{todo.category}</small>
                  <small className="ml-2 text-gray-500">
                    {todo.done ? "Done" : "Not Done"}
                  </small>
                </div>
                <div className="flex items-center">
                  <button
                    onClick={() => deleteTodo(todo.id)}
                    className="text-red-500 mr-2"
                  >
                    <FaTrash />
                  </button>
                  <button
                    onClick={() => updateTodo(todo.id, { done: !todo.done })}
                    className="text-blue-500"
                  >
                    <FaCheck />
                  </button>
                </div>
              </div>
            </li>
          ))}
        </ul>
      ) : (
        <div className="text-gray-700">No todos available.</div>
      )}
      <div className="mt-4 flex">
        <input
          type="text"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          className="flex-1 p-2 border border-gray-300 rounded-l"
          placeholder="New Todo"
        />
        <button
          onClick={() => {
            addTodo(newTodo, "General");
            setNewTodo("");
          }}
          className="bg-blue-500 text-white py-2 px-4 rounded-r flex items-center"
        >
          <FaPlus />
        </button>
      </div>
    </div>
  );
};

export default TodosCard;
