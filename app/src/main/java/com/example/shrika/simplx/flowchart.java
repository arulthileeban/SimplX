package com.example.shrika.simplx;

import android.app.ProgressDialog;
import android.content.Intent;
import android.content.res.AssetManager;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.Typeface;
import android.net.Uri;
import android.os.Handler;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.view.WindowManager;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;


import java.io.IOException;
import java.util.Locale;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Response;

public class flowchart extends AppCompatActivity {
    ImageView img,codeImage;
    TextView code,txt;
    String spath;
    static String respdata="";
    TextView srccode;
    private static int RESULT_LOAD_IMG = 1;
    String imgDecodableString;
    Animation blink;
    private final OkHttpClient client = new OkHttpClient();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getSupportActionBar().hide();
        setContentView(R.layout.activity_flowchart);
        codeImage = (ImageView)findViewById(R.id.codeImage1);
        blink = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.blink);
        AssetManager am = getApplicationContext().getAssets();
        Typeface custom = Typeface.createFromAsset(am,
                String.format(Locale.US, "fonts/%s", "Kelvetica.otf"));
        srccode = (TextView)findViewById(R.id.sourceCode1);
        srccode.setTypeface(custom);

    }
    public void onClick2(View v){
        Intent galleryIntent = new Intent(Intent.ACTION_PICK,
                android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        // Start the Intent
        startActivityForResult(galleryIntent, RESULT_LOAD_IMG);
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        try {
            // When an Image is picked
            codeImage.setVisibility(View.VISIBLE);
            codeImage.startAnimation(blink);
            if (requestCode == RESULT_LOAD_IMG && resultCode == RESULT_OK
                    && null != data) {
                // Get the Image from data
                String filePath1 = null;

                Uri selectedImage = data.getData();
                if (selectedImage != null && "content".equals(selectedImage.getScheme())) {
                    Cursor cursor = this.getContentResolver().query(selectedImage, new String[] { android.provider.MediaStore.Images.ImageColumns.DATA }, null, null, null);
                    cursor.moveToFirst();
                    filePath1 = cursor.getString(0);
                    cursor.close();
                } else {
                    filePath1 = selectedImage.getPath();
                }
                String name = filePath1.substring(filePath1.lastIndexOf("/")+1);
                String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/picture?text+"+name;

                run(url);
                //String filePath = selectedImage.getPath();
                //filePath1=filePath1.replace("document","storage");
                //filePath1=filePath1.replace(":","/");
                // Uri selectedImage = data.getData();
                //String[] filePathColumn = { MediaStore.Images.Media.DATA };
//
                //Cursor cursor = getContentResolver().query(selectedImage,
                //      filePathColumn, null, null, null);
                //cursor.moveToFirst();

                //int columnIndex = cursor.getColumnIndex(filePathColumn[0]);
                //String picturePath = cursor.getString(columnIndex);
                //cursor.close();
                //System.out.println(picturePath);
                //decodeFile(picturePath);

                //spath= filePath1;
                //String[] filePathColumn = { MediaStore.Images.Media.DATA };

               /* // Get the cursor
                Cursor cursor = getContentResolver().query(selectedImage,
                        filePathColumn, null, null, null);
                // Move to first row
                cursor.moveToFirst();

                int columnIndex = cursor.getColumnIndex(filePathColumn[0]);
                imgDecodableString = cursor.getString(columnIndex);
                cursor.close();
                //img = (ImageView) findViewById(R.id.imageView);
                // Set the Image in ImageView after decoding the String
                //img.setImageBitmap(BitmapFactory
                       // .decodeFile(imgDecodableString));
                       */
                Toast.makeText(this, "Image added!",
                        Toast.LENGTH_LONG).show();
                //System.out.println(spath);
                //File f1=new File(picturePath);
                //uploadFile("http:ec2-34-210-99-247.us-west-2.compute.amazonaws.com:5000/picture",f1);
                while(respdata.equals("")){System.out.println(respdata);}

                txt=(TextView)findViewById(R.id.Sourceimg);
                final Handler handler = new Handler();
                handler.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        while(respdata.equals("")){System.out.println(respdata);}

                        AssetManager am1 = getApplicationContext().getAssets();
                        Typeface custom1 = Typeface.createFromAsset(am1,
                                String.format(Locale.US, "fonts/%s", "Kelvetica.otf"));
                        codeImage.clearAnimation();
                        codeImage.setVisibility(View.GONE);
                        txt.setTypeface(custom1);
                        String newCode="";
                        newCode=respdata.replaceAll("\t","\t\t\t\t\t");
                        txt.setText(newCode);
                    }
                }, 2000);

            } else {
                Toast.makeText(this, "You haven't picked Image",
                        Toast.LENGTH_LONG).show();
            }
        } catch (Exception e) {
            Toast.makeText(this, e.toString(), Toast.LENGTH_LONG)
                    .show();
        }

    }
    /*
    public static Boolean uploadFile(String serverURL, File file) throws Exception{

        System.out.println("wrgnslnbglks");
            final MediaType MEDIA_TYPE_PNG = MediaType.parse("image/png");

            RequestBody requestBody = new MultipartBody.Builder()
                    .setType(MultipartBody.FORM)
                    .addFormDataPart("file", file.getName(),
                            RequestBody.create(MediaType.parse("image/jpg"), file))
                    .addFormDataPart("flowchart", "some-value")
                    .build();

            okhttp3.Request request1 = new okhttp3.Request.Builder()
                    .url(serverURL)
                    .post(requestBody)
                    .build();

            OkHttpClient client = new OkHttpClient();
        client.newCall(request1).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                //do failure stuff
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                //do success stuff

               /* Headers responseHeaders = response.headers();
                for (int i = 0, size = responseHeaders.size(); i < size; i++) {
                    System.out.println(responseHeaders.name(i) + ": " + responseHeaders.value(i));
                }
/*              //respdata = response.body().string();
                //System.out.println(respdata);
                //System.out.println(response.body());

                // System.out.println(response);
            }


        });
        return true;
    }*/
    public void run(String Url) throws Exception {

        okhttp3.Request request = new okhttp3.Request.Builder()
                .url(Url)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);

               /* Headers responseHeaders = response.headers();
                for (int i = 0, size = responseHeaders.size(); i < size; i++) {
                    System.out.println(responseHeaders.name(i) + ": " + responseHeaders.value(i));
                }
*/              respdata = response.body().string();
                System.out.println(respdata);
                //txt=(TextView)findViewById(R.id.Sourceimg);
                //AssetManager am1 = getApplicationContext().getAssets();
                //final Typeface custom1 = Typeface.createFromAsset(am1,
                //      String.format(Locale.US, "fonts/%s", "Kelvetica.otf"));


                //System.out.println(response.body());

                // System.out.println(response);
            }
        });

    }

}
