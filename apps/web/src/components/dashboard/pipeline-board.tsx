'use client';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';

const pipelineStages = [
  {
    id: 'applied',
    name: 'Applied',
    count: 45,
    color: 'bg-blue-500',
    candidates: [
      { id: 1, name: 'John Smith', role: 'Senior Engineer', score: 85 },
      { id: 2, name: 'Sarah Johnson', role: 'Product Manager', score: 92 },
      { id: 3, name: 'Mike Davis', role: 'UX Designer', score: 78 },
    ],
  },
  {
    id: 'screening',
    name: 'Screening',
    count: 30,
    color: 'bg-yellow-500',
    candidates: [
      { id: 4, name: 'Emily Wilson', role: 'Data Scientist', score: 88 },
      { id: 5, name: 'David Brown', role: 'Frontend Developer', score: 91 },
    ],
  },
  {
    id: 'interviewing',
    name: 'Interviewing',
    count: 20,
    color: 'bg-purple-500',
    candidates: [
      { id: 6, name: 'Lisa Anderson', role: 'Backend Engineer', score: 87 },
    ],
  },
  {
    id: 'offered',
    name: 'Offered',
    count: 10,
    color: 'bg-green-500',
    candidates: [
      { id: 7, name: 'Tom Martinez', role: 'DevOps Engineer', score: 94 },
    ],
  },
  {
    id: 'hired',
    name: 'Hired',
    count: 5,
    color: 'bg-emerald-500',
    candidates: [
      { id: 8, name: 'Alex Thompson', role: 'Full Stack Developer', score: 96 },
    ],
  },
];

export function PipelineBoard() {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center justify-between">
          <span>Recruitment Pipeline</span>
          <Badge variant="secondary">Total: 110 candidates</Badge>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
          {pipelineStages.map((stage) => (
            <div
              key={stage.id}
              className="bg-gray-50 dark:bg-gray-800 rounded-lg p-4 border border-gray-200 dark:border-gray-700"
            >
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-medium text-gray-900 dark:text-white">
                  {stage.name}
                </h3>
                <Badge className={stage.color}>
                  {stage.count}
                </Badge>
              </div>
              
              <div className="space-y-2">
                {stage.candidates.map((candidate) => (
                  <div
                    key={candidate.id}
                    className="bg-white dark:bg-gray-700 rounded-md p-3 border border-gray-200 dark:border-gray-600 cursor-pointer hover:shadow-sm transition-shadow"
                  >
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-sm font-medium text-gray-900 dark:text-white">
                          {candidate.name}
                        </p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">
                          {candidate.role}
                        </p>
                      </div>
                      <Badge variant="outline" className="text-xs">
                        {candidate.score}
                      </Badge>
                    </div>
                  </div>
                ))}
                
                {stage.candidates.length === 0 && (
                  <div className="text-center py-4 text-gray-500 dark:text-gray-400 text-sm">
                    No candidates
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
