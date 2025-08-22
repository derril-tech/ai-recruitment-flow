'use client';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';

const activities = [
  {
    id: 1,
    type: 'candidate_added',
    message: 'New candidate applied for Senior Software Engineer',
    candidate: 'John Smith',
    role: 'Senior Software Engineer',
    time: '2 minutes ago',
    status: 'new',
  },
  {
    id: 2,
    type: 'interview_scheduled',
    message: 'Interview scheduled for Sarah Johnson',
    candidate: 'Sarah Johnson',
    role: 'Product Manager',
    time: '15 minutes ago',
    status: 'scheduled',
  },
  {
    id: 3,
    type: 'screening_completed',
    message: 'AI screening completed for Mike Davis',
    candidate: 'Mike Davis',
    role: 'UX Designer',
    time: '1 hour ago',
    status: 'completed',
  },
  {
    id: 4,
    type: 'offer_sent',
    message: 'Offer sent to Emily Wilson',
    candidate: 'Emily Wilson',
    role: 'Data Scientist',
    time: '2 hours ago',
    status: 'offered',
  },
  {
    id: 5,
    type: 'candidate_hired',
    message: 'Alex Thompson accepted offer',
    candidate: 'Alex Thompson',
    role: 'Full Stack Developer',
    time: '1 day ago',
    status: 'hired',
  },
];

const getStatusColor = (status: string) => {
  switch (status) {
    case 'new':
      return 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200';
    case 'scheduled':
      return 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200';
    case 'completed':
      return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200';
    case 'offered':
      return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200';
    case 'hired':
      return 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200';
    default:
      return 'bg-gray-100 text-gray-800 dark:bg-gray-900 dark:text-gray-200';
  }
};

export function RecentActivity() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Recent Activity</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {activities.map((activity) => (
            <div
              key={activity.id}
              className="flex items-start space-x-3 p-3 rounded-lg border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
            >
              <div className="flex-shrink-0">
                <div className="w-2 h-2 bg-primary-500 rounded-full mt-2"></div>
              </div>
              
              <div className="flex-1 min-w-0">
                <p className="text-sm text-gray-900 dark:text-white">
                  {activity.message}
                </p>
                <div className="flex items-center justify-between mt-1">
                  <div className="flex items-center space-x-2">
                    <span className="text-xs text-gray-500 dark:text-gray-400">
                      {activity.candidate}
                    </span>
                    <span className="text-xs text-gray-400 dark:text-gray-500">
                      •
                    </span>
                    <span className="text-xs text-gray-500 dark:text-gray-400">
                      {activity.role}
                    </span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <Badge className={getStatusColor(activity.status)}>
                      {activity.status}
                    </Badge>
                    <span className="text-xs text-gray-400 dark:text-gray-500">
                      {activity.time}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        
        <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
          <button className="w-full text-sm text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 font-medium">
            View all activity
          </button>
        </div>
      </CardContent>
    </Card>
  );
}
