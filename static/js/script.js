// window.addEventListener('DOMContentLoaded', function () {
//       let avatar = document.getElementById('avatar');
//       let image = document.getElementById('image');
//       let input = document.getElementById('input');
//       let $progress = $('.progress');
//       let $progressBar = $('.progress-bar');
//       let $alert = $('.alert');
//       let $modal = $('#modal');
//       let cropper;
//
//       $('[data-toggle="tooltip"]').tooltip();
//
//       input.addEventListener('change', function (e) {
//         let files = e.target.files;
//         let done = function (url) {
//           input.value = '';
//           image.src = url;
//           $alert.hide();
//           $modal.modal('show');
//         };
//         let reader;
//         let file;
//         let url;
//
//         if (files && files.length > 0) {
//           file = files[0];
//
//           if (URL) {
//             done(URL.createObjectURL(file));
//           } else if (FileReader) {
//             reader = new FileReader();
//             reader.onload = function (e) {
//               done(reader.result);
//             };
//             reader.readAsDataURL(file);
//           }
//         }
//       });
//
//       $modal.on('shown.bs.modal', function () {
//         cropper = new Cropper(image, {
//           aspectRatio: 1,
//           viewMode: 3,
//         });
//       }).on('hidden.bs.modal', function () {
//         cropper.destroy();
//         cropper = null;
//       });
//
//       document.getElementById('crop').addEventListener('click', function () {
//         let initialAvatarURL;
//         let canvas;
//
//         $modal.modal('hide');
//
//         if (cropper) {
//           canvas = cropper.getCroppedCanvas({
//             width: 160,
//             height: 160,
//           });
//           initialAvatarURL = avatar.src;
//           avatar.src = canvas.toDataURL();
//           $progress.show();
//           $alert.removeClass('alert-success alert-warning');
//           canvas.toBlob(function (blob) {
//             let formData = new FormData();
//
//             formData.append('avatar', blob, 'avatar.jpg');
//             $.ajax('https://jsonplaceholder.typicode.com/posts', {
//               method: 'POST',
//               data: formData,
//               processData: false,
//               contentType: false,
//
//               xhr: function () {
//                 let xhr = new XMLHttpRequest();
//
//                 xhr.upload.onprogress = function (e) {
//                   let percent = '0';
//                   let percentage = '0%';
//
//                   if (e.lengthComputable) {
//                     percent = Math.round((e.loaded / e.total) * 100);
//                     percentage = percent + '%';
//                     $progressBar.width(percentage).attr('aria-valuenow', percent).text(percentage);
//                   }
//                 };
//
//                 return xhr;
//               },
//
//               success: function () {
//                 $alert.show().addClass('alert-success').text('Upload success');
//               },
//
//               error: function () {
//                 avatar.src = initialAvatarURL;
//                 $alert.show().addClass('alert-warning').text('Upload error');
//               },
//
//               complete: function () {
//                 $progress.hide();
//               },
//             });
//           });
//         }
//       });
//     });