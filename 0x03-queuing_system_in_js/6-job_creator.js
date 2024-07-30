import { createQueue } from 'kue';

const queue = createQueue();

// job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification!',
};

// create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData);

job
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });
