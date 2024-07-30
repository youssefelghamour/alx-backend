import { createQueue } from 'kue';

const queue = createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// process jobs from the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  // extract job data
  const { phoneNumber, message } = job.data;

  // call the function to send notification
  sendNotification(phoneNumber, message);

  // mark job as done
  done();
});
