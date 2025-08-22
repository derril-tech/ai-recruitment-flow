'use client';

import { UsersIcon, BriefcaseIcon, CalendarIcon, CheckCircleIcon } from '@heroicons/react/24/outline';

const stats = [
  {
    name: 'Active Candidates',
    value: '1,234',
    change: '+12%',
    changeType: 'positive',
    icon: UsersIcon,
  },
  {
    name: 'Open Roles',
    value: '45',
    change: '+3',
    changeType: 'positive',
    icon: BriefcaseIcon,
  },
  {
    name: 'Interviews This Week',
    value: '28',
    change: '-2',
    changeType: 'negative',
    icon: CalendarIcon,
  },
  {
    name: 'Hired This Month',
    value: '12',
    change: '+4',
    changeType: 'positive',
    icon: CheckCircleIcon,
  },
];

export function QuickStats() {
  return (
    <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
      {stats.map((item) => (
        <div
          key={item.name}
          className="relative overflow-hidden rounded-lg bg-white dark:bg-gray-800 px-4 pb-12 pt-5 shadow-soft border border-gray-200 dark:border-gray-700"
        >
          <dt>
            <div className="absolute rounded-md bg-primary-500 p-3">
              <item.icon className="h-6 w-6 text-white" aria-hidden="true" />
            </div>
            <p className="ml-16 truncate text-sm font-medium text-gray-500 dark:text-gray-400">
              {item.name}
            </p>
          </dt>
          <dd className="ml-16 flex items-baseline pb-6 sm:pb-7">
            <p className="text-2xl font-semibold text-gray-900 dark:text-white">
              {item.value}
            </p>
            <p
              className={`ml-2 flex items-baseline text-sm font-semibold ${
                item.changeType === 'positive'
                  ? 'text-success-600 dark:text-success-400'
                  : 'text-error-600 dark:text-error-400'
              }`}
            >
              {item.change}
            </p>
          </dd>
        </div>
      ))}
    </div>
  );
}
