import { createQueue } from 'kue';

// array for blacklisted phone numbers
const blacklistedNumbers = [
  '4153518780',
  '4153518781'
];

// function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // track progress to 0%
  job.progress(0, 100);
  
  // check if phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // fail the job if blacklisted and call done
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // track progress to 50%
  job.progress(50, 100);

  // log notification details
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // mark job as complete
  done();
}

const queue = createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
