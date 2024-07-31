import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

describe('createPushNotificationsJobs', function() {
  let queue;

  before(() => {
    queue = createQueue();
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Test message 1' },
      { phoneNumber: '4153518781', message: 'Test message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobIds = queue.testMode.jobs.map(job => job.id);
    expect(jobIds).to.have.lengthOf(2);
  });
});
