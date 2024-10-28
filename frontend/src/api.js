
export async function fetchTasks() {
  const response = await fetch('http://localhost:8000/tasks/');
  return await response.json();
}
