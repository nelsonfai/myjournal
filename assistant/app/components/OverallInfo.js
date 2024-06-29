export default function OverallInfo({
    tasksDone,
    projectsStopped,
    projectsCompleted,
  }) {
    return (
      <div className="bg-gray-800 rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold text-white mb-4">
          Overall Information
        </h2>
        <div className="flex justify-between">
          <div>
            <p className="text-4xl font-bold text-white">{tasksDone}</p>
            <p className="text-sm text-gray-400">Tasks done for all time</p>
          </div>
          <div>
            <p className="text-4xl font-bold text-white">{projectsStopped}</p>
            <p className="text-sm text-gray-400">Projects are stopped</p>
          </div>
          <div>
            <p className="text-4xl font-bold text-white">{projectsCompleted}</p>
            <p className="text-sm text-gray-400">Projects are completed</p>
          </div>
        </div>
      </div>
    );
  }
  