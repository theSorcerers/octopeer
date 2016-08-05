class Api::EventTypesController < ApplicationController
  before_action :set_event_type, only: :show

  def index
    @event_types = EventType.all

    render json: @event_types
  end

  def show
    render json: @event_type
  end

  def create
    @event_type = EventType.new(event_type_params)

    if @event_type.save
      render json: @event_type, status: :created
    else
      render json: @event_type.errors, status: :unprocessable_entity
    end
  end

  private

  def set_event_type
    @event_type = EventType.find(params[:id])
  end

  def event_type_params
    params.require(:event_type).permit(:id, :name)
  end
end
