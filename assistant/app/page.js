// pages/index.js
import OverallInfo from "./components/OverallInfo";
import NotesCard from "./components/NoteCard";
import TodosCard from "./components/TodosCard";
import Layout from "./components/Layout";
import './globals.css'

// Import other components

export default function Home() {
  return (
    <Layout>
      <div className="grid grid-cols-3 gap-6">
        <div className="col-span-2 bg-red-400">
          <OverallInfo
            tasksDone={43}
            projectsStopped={2}
            projectsCompleted={11}
          />
          {/* Add WeeklyProgress and MonthProgress components */}
        </div>
        <div className="space-y-6">
          <NotesCard />
          <TodosCard />

          {/* Add MonthGoals component */}
        </div>
      </div>
      <div className="mt-6">{/* Add TaskInProcess component */}</div>
      <div className="mt-6">{/* Add LastProjects component */}</div>
      </Layout>
  );
}
