---
title: Assignment 1
subtitle: Computer performance, reliability, and scalability calculation
author:  Michael Hotaling
---

## 1.2 

#### a. Data Sizes

| Data Item                                  | Size per Item | Calculation                                      | Source | 
|--------------------------------------------|--------------:|-------------------------------------------------:|-------:|
| 128 character message.                     | 112 Bytes     | 128 characters * 7 bits/character * 1/8 Byte/bit | [link](https://www.sidehustlenation.com/how-much-does-a-text-message-really-cost/)
| 1024x768 PNG image                         | 457 kB        |                                                  | [link](https://toolstud.io/photo/megapixel.php?width=1024&height=768&compare=video&calculate=compressed#calculate) |
| 1024x768 RAW image                         | 1.57 MB       |                                                  | [link](https://toolstud.io/photo/megapixel.php?width=1024&height=768&compare=video&calculate=uncompressed#calculate)
| HD (1080p) HEVC Video (15 minutes)         | 0.375089 GB   | DVD MPEG2 (compressed)                           | [link](https://toolstud.io/video/filesize.php?dimensions_w=1920&dimensions_h=1080&framerate=29.97&timeduration=15&timeduration_unit=minutes)
| HD (1080p) Uncompressed Video (15 minutes) | 7.93 GB       | DVD MPEG2 (uncompressed)                         | [link](https://toolstud.io/video/filesize.php?dimensions_w=1920&dimensions_h=1080&framerate=29.97&timeduration=15&timeduration_unit=minutes)
| 4K UHD HEVC Video (15 minutes)             | 1.49941 GB    | DVD MPEG2 (compressed)                           | [link](https://toolstud.io/video/filesize.php?dimensions_w=3840&dimensions_h=2160&framerate=29.97&timeduration=15&timeduration_unit=minutes)
| 4k UHD Uncompressed Video (15 minutes)     | 31.7 GB       | DVD MPEG2 (uncompressed)                         | [link](https://toolstud.io/video/filesize.php?dimensions_w=3840&dimensions_h=2160&framerate=29.97&timeduration=15&timeduration_unit=minutes)
| Human Genome (Uncompressed)                | 200 GB        | Whole Genome - Strand NGS Size                   | [link](https://www.strand-ngs.com/support/ngs-data-storage-requirements)

#### b. Scaling

|                                           | Size       | # HD | 
|-------------------------------------------|-----------:|-----:|
| Daily Twitter Tweets (Uncompressed)       | 56 GB      | 1      |
| Daily Twitter Tweets (Snappy Compressed)  | 37 GB      | 1      |
| Daily Instagram Photos                    | 34 TB      | 10     |
| Daily YouTube Videos                      | 1000 TB    | 300    |
| Yearly Twitter Tweets (Uncompressed)      | 20.5 TB    | 7      |
| Yearly Twitter Tweets (Snappy Compressed) | 13.5 TB    | 5      |
| Yearly Instagram Photos                   | 12418 TB   | 3726   |
| Yearly YouTube Videos                     | 365250 TB  | 110000 |

#### c. Reliability

Assuming average failure rate of [0.81%](https://www.backblaze.com/blog/backblaze-hard-drive-stats-q2-2020/)

|                                    | # HD   | # Failures |
|------------------------------------|-------:|-----------:|
| Twitter Tweets (Uncompressed)      | 7      | 1          |
| Twitter Tweets (Snappy Compressed) | 5      | 1          |
| Instagram Photos                   | 3726   | 30         |
| YouTube Videos                     | 110000 | 213        |

#### d. Latency

|                           | One Way Latency      | Source |
|---------------------------|---------------------:|-------:|
| Los Angeles to Amsterdam  | 70 ms                | [link](https://wondernetwork.com/pings/Los%20Angeles/Amsterdam)
| Low Earth Orbit Satellite | 32 ms                | [link](https://arstechnica.com/information-technology/2019/07/onewebs-low-earth-satellites-hit-400mbps-and-32ms-latency-in-new-test/)
| Geostationary Satellite   | 270 ms               | [link](https://www.satellitetoday.com/telecom/2009/09/01/minimizing-latency-in-satellite-networks/)
| Earth to the Moon         | 1250 ms              | [link](https://space.stackexchange.com/questions/35590/what-is-the-lowest-latency-achievable-in-reliable-earth-moon-communications)
| Earth to Mars             | 13 minutes           | [link](https://blogs.esa.int/mex/2012/08/05/time-delay-between-mars-and-earth/)

```python
110000 * 0.0081
```

```python

```
