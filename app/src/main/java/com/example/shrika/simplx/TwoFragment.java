package com.example.shrika.simplx;

import android.app.TabActivity;
import android.content.res.AssetManager;
import android.graphics.Typeface;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.view.ViewPager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.util.Locale;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Response;

/**
 * Created by adminlap on 3/6/17.
 */
public class TwoFragment extends Fragment {
    public TwoFragment() {
        // Required empty public constructor

    }
    TextView srccode;
    ImageView image,tick;
    ViewPager mviewPager;
    private final OkHttpClient client = new OkHttpClient();
    String respdata="";
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_two,container,false);
        mviewPager = (ViewPager) getActivity().findViewById(R.id.viewpager);
        srccode = (TextView) view.findViewById(R.id.srcCode);
        image = (ImageView) view.findViewById(R.id.algSourcecode);
        tick = (ImageView) getActivity().findViewById(R.id.tick);
        AssetManager am = getActivity().getApplicationContext().getAssets();
        Typeface custom = Typeface.createFromAsset(am,
                String.format(Locale.US, "fonts/%s", "Kelvetica.otf"));
        srccode.setTypeface(custom);
        tick.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/voice";
                    run(url);
                    Thread thread1 = new Thread(new Runnable(){
                        @Override
                        public void run(){
                            while (respdata.equals("")){}
                            getActivity().runOnUiThread(new Runnable() {
                                @Override
                                public void run() {
                                    image.setVisibility(View.GONE);
                                    mviewPager.setCurrentItem(2,true);
                                    String newCode="";
                                    newCode=respdata.replaceAll("\t","\t\t\t\t\t");
                                    srccode.setText(newCode);

                                }
                            });


                        }
                    });
                    thread1.start();
                }catch (Exception e){

                }
            }
        });

        return view;
    }
    public void run(String Url) throws Exception {

        okhttp3.Request request = new okhttp3.Request.Builder()
                .url(Url)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                Toast.makeText(getContext(), "request failed", Toast.LENGTH_LONG).show();
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);

                respdata = response.body().string();
                System.out.println(respdata);


            }
        });
    }

}
