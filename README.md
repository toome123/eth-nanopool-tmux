# Ethereum mining @ nanopool.org tmux session

![](https://raw.githubusercontent.com/gsora/eth-nanopool-tmux/master/session-screenshot.png)

This repository contains a tmux session built expressly for CUDA (NVidia) Ethereum mining on nanopool.org.

Can be adapted easily to OpenCL, removing the `nvidia-smi` pane.


## Layout

```
+----------+---------+
|          |         |
|ethminer  |nanopool |
|          |monitor  |
|          |         |
+----------+---------+
|          |         |
|nvidia-smi|htop     |
|          |         |
|          |         |
+----------+---------+
```

The session will be named `mining-session`.

## Requirements

- `python3` 
- `python-requests`
- `tmux`
- `nvidia-smi`

Check for these requirements on your distribution.

## Configuration

All the configuration happends into the `start-mining` script:

|Required|Option|Description
|------|-----|-----|
|yes|`ETH_ADDRESS`|your Ethereum address|
|yes|`MINER_PATH`|your miner path, can be absolute or relative|
|no|`MINER_NAME`|a miner name, useful if you have multiple miners on the same account|
|yes|`MINER_PARAMS`|parameters for your miner|

## Usage

Simply execute it as a bash script:

```
$ bash ./start-mining
```

## Donations

If you want to thank me for my work, you can send some Ether here: `0x4521B733c91b517F6bCed1bEa5f9e02Fa1AFbaa6` :)
