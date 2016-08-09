class Api::FilePositionsController < ApplicationController
  before_action :set_file_position, only: :show

  def index
    @file_positions = FilePosition.all

    render json: @file_positions
  end

  def show
    render json: @file_position
  end

  def create
    @file_position = FilePosition.new(file_position_params)

    if @file_position.save
      render json: @file_position, status: :created
    else
      render json: @file_position.errors, status: :unprocessable_entity
    end
  end

  private

  def set_file_position
    @file_position = FilePosition.find(params[:id])
  end

  def file_position_params
    params.require(:file_position).permit(:semantic_event_id, :commit_hash, :filename, :line_number)
  end
end
